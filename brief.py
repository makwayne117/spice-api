def brief_parse():
    from subprocess import check_output
    # print out summary of file
    out = check_output(["brief", "kernels/jup068.bsp"])

    # convert to string
    c = str(out)
    print(c)
    # add 7 to start the split to s
    s = c.find("Bodies")
    e = c.find("Start")

    # slice the string
    sp = c[s + 8:e]

    # remove the n string
    rn = sp.replace("n", "")

    # remove the \
    rs = rn.replace("\ ", "")

    # split the string
    f = rs.split()
    # empty array
    arr = []
    # remove any barycenters and numbers
    for x in range(len(f)):
        if (f[x] != "BARYCENTER" and f[x][0] != "("):
            arr.append(f[x])
    print(arr)
    return arr
if __name__ == "__main__":
    brief_parse()