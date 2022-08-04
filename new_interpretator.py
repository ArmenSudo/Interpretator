import sys
import variables


def main(argv):
    err_line = 0
    f = open(argv[0], 'r')
    lines = f.readlines()
    for line in lines:
        err_line += 1
        line = line.strip()
        if len(line) == 0:
            continue
        while True:
            line = line.strip()
            variables.command = line[:3]
            if variables.command in variables.syntax and line.count(";") > 0:
                # ________________________ tiv _______________________________________________

                if variables.command == 'tiv' and line[3] == ' ':
                    if line.count("=") >= 1:
                        var_name = line[3:line.index("=")].strip()
                        var_value = line[line.index("=") + 1: line.index(";")].strip()
                        if len(var_name) > 0 and len(var_value) > 0:
                            if var_name.count(" ") > 0 or var_value.count(" ") > 0:
                                raise ValueError(f"Chisht Gri :) tox {err_line}")
                            else:
                                try:
                                    variables.name_space[var_name] = int(var_value)
                                except:
                                    raise TypeError(f"Sxales gre  tox {err_line}")
                        else:
                            raise TypeError(f"Sxales gre  tox {err_line}")
                    else:
                        raise TypeError(f"Sxales gre  tox {err_line}")

                # ________________________ tiv _______________________________________________

                # ________________________ float tiv _______________________________________________

                elif variables.command == 'ftv' and line[3] == ' ':
                    if line.count("=") >= 1:
                        var_name = line[3:line.index("=")].strip()
                        var_value = line[line.index("=") + 1: line.index(";")].strip()
                        if len(var_name) > 0 and len(var_value) > 0:
                            if var_name.count(" ") > 0 or var_value.count(" ") > 0:
                                raise ValueError(f"Chisht Gri :) tox {err_line}")
                            else:
                                try:
                                    variables.name_space[var_name] = float(var_value)
                                except:
                                    raise TypeError(f"Sxales gre  tox {err_line}")
                        else:
                            raise TypeError(f"Sxales gre  tox {err_line}")
                    else:
                        raise TypeError(f"Sxales gre  tox {err_line}")

                # ________________________ float tiv _______________________________________________

                # ________________________ tox _______________________________________________

                elif variables.command == 'tox' and line[3] == ' ':
                    if line.count("=") >= 1:
                        var_name = line[3:line.index("=")].strip()
                        var_value = line[line.index("=") + 1: line.index(";")].strip()
                        if var_name.count(" "):
                            raise TypeError(f"Sxales gre tox {err_line}")
                        if len(var_name) > 0 and len(var_value) > 0 and var_value[0] == var_value[-1] and (
                                var_value[0] == "'" or var_value[0] == '"'):
                            if var_value.count("'") > 1 or var_value.count("\"") > 1:
                                if var_value.count("'") % 2 == 1 or var_value.count("\"") % 2 == 1:
                                    raise ValueError(f"Chisht Gri :) tox {err_line}")
                                else:
                                    try:
                                        variables.name_space[var_name] = str(var_value)[1:-1]
                                    except:
                                        raise TypeError(f"Sxales gre tox {err_line}")
                            else:
                                raise TypeError(f"Sxales gre tox {err_line}")
                        else:
                            raise TypeError(f"Sxales gre tox {err_line}")
                    else:
                        raise TypeError(f"Sxales gre tox {err_line}")

                # ________________________ tox _______________________________________________

                # ________________________ tpel _______________________________________________

                elif variables.command == 'tpe':
                    if line.count(">>") >= 1:
                        value = line[line.index(">>") + 2: line.index(";")].strip()
                        if len(value) > 0 and value[0] == value[-1] and (value[0] == "'" or value[0] == '"'):
                            print(value)
                        elif len(value) > 0 and value.lstrip('-').isnumeric() or isfloat(value.lstrip('-')):
                            print(value)
                        else:
                            try:
                                print(eval(value))
                            except (NameError, SyntaxError):
                                hav = ''
                                arr = []
                                for x in value:
                                    if x == '+' or x == "*":
                                        arr.append(hav)
                                        arr.append(x)
                                        hav = ''
                                    elif x == " ":
                                        continue
                                    else:
                                        hav += x
                                else:
                                    arr.append(hav)
                                for x in variables.name_space.keys():
                                    for index, val in enumerate(arr):
                                        if x == val:
                                            arr[index] = str(variables.name_space[x]) if (type(variables.name_space[x]) == int) or (
                                                    type(variables.name_space[x]) == float) else f"'{variables.name_space[x]}' "
                                try:
                                    print(eval(''.join(arr)))
                                except (TypeError, NameError, SyntaxError):
                                    raise TypeError(f"Sxales gre tox {err_line}")

                    else:
                        raise TypeError(f"Sxales gre tox {err_line}")

                # ________________________ tpel _______________________________________________

                # ________________________ payman _______________________________________________

                elif variables.command == 'ete' and line[3] == " ":
                    if line.count("apa") >= 1:

                        payman = line[3:line.index("apa")].strip()
                        gorcoxutyun = line[line.index("apa") + 3: line.rindex(";") + 1].strip()
                        try:
                            try:
                                variables.flag = eval(f"bool({payman})")
                            except:
                                arr = payman.split()

                                for x in variables.name_space.keys():
                                    for index, val in enumerate(arr):
                                        if x == val:
                                            arr[index] = str(variables.name_space[x]) if (type(variables.name_space[x]) == int) or (
                                                    type(variables.name_space[x]) == float) else f"'{variables.name_space[x]}'"

                                variables.flag = eval(f"bool({''.join(arr)})")
                            # print(variables.flag)
                            if variables.flag:
                                line = gorcoxutyun
                                command = line[:3]
                                continue
                            else:
                                break
                        except NameError:
                            raise TypeError(f"sxales gre tox {err_line}")

                    else:
                        raise TypeError(f"Sxales gre tox {err_line}")
                # ________________________ payman _______________________________________________


                # ________________________ hak _______________________________________________
                elif variables.command == 'hak' and not variables.flag and line[3] == ' ':
                    line = line[line.index('hak')+3:line.rindex(";")+1].strip()
                    continue

            line = line[line.index(';') + 1:]
            if len(line) < 3:
                break

    print(variables.name_space)


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    main(sys.argv[1:])
