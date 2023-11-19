from pathlib import Path
import subprocess


def get_tasks_sets(dir):
    return [str(a.name).replace('.in', '') for a in Path(dir).glob('*in')]


def execute_task(dir):
    task_sets = get_tasks_sets(dir)
    for task_set in task_sets:
        try:
            with open(Path(dir, f'{task_set}.in')) as f_in, open(Path(dir, f'{task_set}.out'), 'w') as f_out:
                arg = [x for x in dir.iterdir() if str(x).endswith(f'{task_set}.arg')]  #  arg = [x for x in dir.iterdir() if str(x).endswith(f'{task_set}.arg')]
                if not arg:
                    arg = [x for x in dir.iterdir() if str(x).endswith('fsa_description.arg')] # arg = Path(dir, 'fsa_description.arg') #
                if str(dir).startswith('TaskH'):
                    compilation_command = ['thraxcompiler', f'--input_grammar={Path(dir, "grammar.grm")}',
                                           f'--output_far={Path(dir, "grammar.far")}']
                    process = subprocess.Popen(compilation_command, stdout=subprocess.DEVNULL,
                                               stderr=subprocess.DEVNULL)
                    process.wait()
                    command = ['thraxrewrite-tester', f'--far={Path(dir, "grammar.far")}', f'--rules=FinalRule']
                else:
                    command = ['python3', Path(dir, 'run.py')]
                    if len(arg) != 0:
                        command.append(arg[0])
                process = subprocess.Popen(command,
                                           stdin=f_in,
                                           stdout=f_out,
                                           stderr=subprocess.DEVNULL)
                process.wait()
                f_out.flush()
        except:
            pass


def get_index():
    return int(Path.cwd().name.split('-')[-1][1:30])


def is_task_set_correct(dir, task_set):
    try:
        with open(Path(dir, f'{task_set}.out')) as f_out, open(Path(dir, f'{task_set}.exp')) as f_exp:
            f_out_lines = ''.join(f_out.readlines())
            f_exp_lines = ''.join(f_exp.readlines())
            return f_out_lines == f_exp_lines
    except:
        pass


def is_task_correct(dir):
    task_sets = get_tasks_sets(dir)
    for task_set in task_sets:
        if not is_task_set_correct(dir, task_set):
            return False
    return True


def does_task_match_index(dir, index):
    with open(Path(dir, f'description.txt')) as f_in:
        lines = f_in.readlines()
        remainder_lines = [x for x in lines if x.startswith('REMAINDER')]
        if len(remainder_lines) == 0:
            return True
        else:
            remainder, modulus = remainder_lines[0].split(' ')[-1].split('/')
            remainder = int(remainder)
            modulus = int(modulus)
            return (index % modulus) == remainder


def get_tasks(index):
    all_tasks = Path('.').glob('Task*')
    return [task for task in all_tasks if does_task_match_index(task, index)]


def execute_all_tasks(tasks):
    for task in tasks:
        execute_task(task)


def get_task_points(dir):
    with open(Path(dir, 'description.txt')) as f_in:
        lines = f_in.readlines()
        points = int([x for x in lines if x.startswith('POINTS')][0].split(' ')[-1].rstrip())
        return points


def get_report(tasks):
    report = dict()
    for task in tasks:
        if is_task_correct(task):
            report[task] = get_task_points(task)
        else:
            report[task] = 0
    return report


def print_report(report):
    for k in sorted(report):
        print(f'{k}: {report[k]}')
    print('')
    print(f'SUMMARY: {sum(report.values())}')


INDEX = get_index()
tasks = get_tasks(INDEX)
execute_all_tasks(tasks)
report = get_report(tasks)
print_report(report)
