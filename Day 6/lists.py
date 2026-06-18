# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    lst = []

    """
    Read in the value of N followed by N lines of commands.
    Each command can be one of several list operations (insert, append, remove, etc.).

    Since there are N commands, we use a for loop to repeat the same process N times.
    In each iteration, we read one command, interpret it, and perform the corresponding operation
    on the list in the exact order given.

    This ensures every command is executed step by step on the same list.
    """
    """
    The underscore (_) is used as a throwaway variable to show that
    the value is intentionally ignored.
    """
    for _ in range(N):
        cmd = input().split()
        """
        Each input line is split into a list called cmd.

        cmd[0] always represents the command name (such as insert, append, remove, print, sort, pop, or reverse).

        The remaining elements in cmd (like cmd[1], cmd[2]) are the values required for that command.

        We use cmd[0] to decide which operation to perform on the list, and then use the other elements
        as inputs for that specific operation.
        """
        if cmd[0] == 'insert':
            lst.insert(int(cmd[1]), int(cmd[2]))

        elif cmd[0] == 'print':
            print(lst)

        elif cmd[0] == 'remove':
            lst.remove(int(cmd[1]))

        elif cmd[0] == 'append':
            lst.append(int(cmd[1]))

        elif cmd[0] == 'sort':
            lst.sort()

        elif cmd[0] == 'pop':
            lst.pop()

        elif cmd[0] == 'reverse':
            lst.reverse()
