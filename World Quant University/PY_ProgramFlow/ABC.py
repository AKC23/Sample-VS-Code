
# def print_todo(watch_tv, read  = False , eat, sleep):      # wrong approach
def print_todo(watch_tv, read, eat, sleep = False):
    print('I need to:')
    if watch_tv:
        print('  watch_tv')
    if read:
        print('  read')
    if eat:
        print('  eat')
    if sleep:
        print('  sleep')

def main():        
    print_todo(False, True, True)
    # print_todo_args(1)

if __name__ == '__main__':
    main()

def print_todo_args(*args):
    print('I need to:')
    for arg in args:
        print('  ' + arg)
print_todo_args('watch_tv', 'read', 'eat', 'sleep')