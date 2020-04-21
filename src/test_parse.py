
def test():
    testfilename    = "test.txt"
    outputfilename  = "all_all.txt"
    outcome         = ""
    failed_line     = ""
    fail_count      = 0
    t               = open(testfilename, 'r').readlines()
    test_count      = len(t)

    test_lines      = []
    for line in t:
        test_lines.append(line.split())
    o               = open(outputfilename, 'r').readlines()
    output_count    = len(o)

    output_lines    = []
    for line in o:
        output_lines.append(line.split())

    fail_list = []
    for test in test_lines:
        if test in output_lines:
            pass
        else:
            fail_count += 1
            fail_list.append(test)
    if fail_count > 0:
        outcome = "Failure:  {fc} out of {tfc} of the test lines are not present in the output!"
    if fail_count == 0:
        outcome = "Success:  It seems all {tfc} test lines are present in the {tc} output lines!"
    fail_list_outcome = "Failed test: {}"
    print(outcome.format(fc=fail_count, tfc=test_count, tc=output_count))
    for x in fail_list:
        print(fail_list_outcome.format(x))
    '''
    txt = "For only {price:.2f} dollars!"
    print(txt.format(price = 49))
    '''