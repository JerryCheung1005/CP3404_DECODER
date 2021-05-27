string = 'buebrrmlqdkrhyirlaxalsjciyspccfzgiipxuxqfkflvqzyevrzzlxhyqkghuwwkclvjtvplvpikghuwglaahwzvebzpokghumbtcgamjvqvyirzrvhvriczpwhiympsbvqvyskjckcmqvqtuhweqnyebtcypvgkjrsekjatufsdywlawkfklkoibmvffvydprukfxyyzvqyvvsoyfwpsucyhyzkggnsbgyrtibkmkprgzbxyxfrbbukqfsekvsjseambrdbuioebhynozjllrhvlvlebfralvgfjnamceglasdimophsrlbugserbcigtfxtihfpxdefunxvtzvrahxtfjevahyckbpsjdhyilrkisissyrvjtvplhjsvbuhgyjwlaiakftaezcmpzfipckzebuqxspsiqmvgfvymltffdbsigrzhbxsraavxvvpuhwsumgwvsmghbwrvyeprujygfsbvatuzwvumoigvnkvjwccliitfpxlrurebukweznzmbvqldmhyralmbugophirjtiymvphywscjxyawkftzlouwkltikympsbtyghpgfzxipotiepwhvbyysawsmbvsrsvamcenkvgsvbbukgzltkhwkghugfvbbagoibklkwjrkhxwflvhrpvsllhojnkvstfdbkibkgmfebuqxjyfzrrmsfgyrtibkgghwwdgehvarlglvsjakvagvpopgsjpxxywictsppzbwlvgkmiseqvralmfgyrtibkgglwqimpdlwtfbziwkfxyvswsgkirfpwltcjgmlhrvnxuhweehuxvvynjxwflhbxqfkxhphvpghxscwbuwiiygjiqrlulstwcklhhfntyxwtgihrhjggzmhlympsbjualvskfxfwiwdxypcjqtzefvqnsxcwsgmewizxoejzmny'

a1 = []
b2 = []
c3 = []
d4 = []
e5 = []
f6 = []

aa = {}
bb = {}
cc = {}
dd = {}
ee = {}
ff = {}

# Part 1: Add into a list
# 1
for first in range(1000):
    try:
        if (first + 1) % 6 == 1:
            a1.append(string[first])
    except:
        pass

# 2
for second in range(1000):
    try:
        if (second + 1) % 6 == 2:
            b2.append(string[second])
    except:
        pass

# 3
for third in range(1000):
    try:
        if (third + 1) % 6 == 3:
            c3.append(string[third])
    except:
        pass

# 4
for fourth in range(1000):
    try:
        if (fourth + 1) % 6 == 4:
            d4.append(string[fourth])
    except:
        pass

# 5
for fifth in range(1000):
    try:
        if (fifth + 1) % 6 == 5:
            e5.append(string[fifth])
    except:
        pass

# 6
for sixth in range(1000):
    try:
        if (sixth + 1) % 6 == 0:
            f6.append(string[sixth])
    except:
        pass

    # Part 2: frequency table
print(a1)
print(b2)
print(c3)
print(d4)
print(e5)
print(f6)


def Count(group, dictionary):
    A = 0
    B = 0
    C = 0
    D = 0
    E = 0
    F = 0
    G = 0
    H = 0
    I = 0
    J = 0
    K = 0
    L = 0
    M = 0
    N = 0
    O = 0
    P = 0
    Q = 0
    R = 0
    S = 0
    T = 0
    U = 0
    V = 0
    W = 0
    X = 0
    Y = 0
    Z = 0
    # group is lists
    for Aa in group:
        if Aa == 'a':
            A = A + 1
    for Bb in group:
        if Bb == 'b':
            B += 1
    for Cc in group:
        if Cc == 'c':
            C += 1
    for Dd in group:
        if Dd == 'd':
            D += 1
    for Ee in group:
        if Ee == 'e':
            E += 1
    for Ff in group:
        if Ff == 'f':
            F += 1
    for Gg in group:
        if Gg == 'g':
            G += 1
    for Hh in group:
        if Hh == 'h':
            H += 1
    for Ii in group:
        if Ii == 'i':
            I += 1
    for Jj in group:
        if Jj == 'j':
            J += 1
    for Kk in group:
        if Kk == 'k':
            K += 1
    for Ll in group:
        if Ll == 'l':
            L += 1
    for Mm in group:
        if Mm == 'm':
            M += 1
    for Nn in group:
        if Nn == 'n':
            N += 1
    for Oo in group:
        if Oo == 'o':
            O += 1
    for Pp in group:
        if Pp == 'p':
            P += 1
    for Qq in group:
        if Qq == 'q':
            Q += 1
    for Rr in group:
        if Rr == 'r':
            R += 1
    for Ss in group:
        if Ss == 's':
            S += 1
    for Tt in group:
        if Tt == 't':
            T += 1
    for Uu in group:
        if Uu == 'u':
            U += 1
    for Vv in group:
        if Vv == 'v':
            V += 1
    for Ww in group:
        if Ww == 'w':
            W += 1
    for Xx in group:
        if Xx == 'x':
            X += 1
    for Yy in group:
        if Yy == 'y':
            Y += 1
    for Zz in group:
        if Zz == 'z':
            Z += 1
    dictionary['a'] = A
    dictionary['b'] = B
    dictionary['c'] = C
    dictionary['d'] = D
    dictionary['e'] = E
    dictionary['f'] = F
    dictionary['g'] = G
    dictionary['h'] = H
    dictionary['i'] = I
    dictionary['j'] = J
    dictionary['k'] = K
    dictionary['l'] = L
    dictionary['m'] = M
    dictionary['n'] = N
    dictionary['o'] = O
    dictionary['p'] = P
    dictionary['q'] = Q
    dictionary['r'] = R
    dictionary['s'] = S
    dictionary['t'] = T
    dictionary['u'] = U
    dictionary['v'] = V
    dictionary['w'] = W
    dictionary['x'] = X
    dictionary['y'] = Y
    dictionary['z'] = Z

    return sorted(dictionary.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    # A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z


print("First-----------------------")
print('first', a1)
print("Second-----------------------")
print('second', b2)
print("Third-----------------------")
print('third', c3)
print("Fourth-----------------------")
print('fourth', d4)
print("Fifth-----------------------")
print('fifth', e5)
print("Sixth-----------------------")
print('sixth', f6)

with open('CNM_JB.txt', 'a') as in_file:
    # 1
    Count(a1, aa)
    in_file.write("First-----------------------\n")
    in_file.write(str(a1))
    in_file.write('\n')
    in_file.write(str(Count(a1, aa)))
    in_file.write('\n')

    in_file.write('\n')

    # 2
    Count(b2, bb)
    in_file.write("Second----------------------\n")
    in_file.write(str(b2))
    in_file.write('\n')
    in_file.write(str(Count(b2, bb)))
    in_file.write('\n')

    in_file.write('\n')

    # 3
    Count(c3, cc)
    in_file.write("Third-----------------------\n")
    in_file.write(str(c3))
    in_file.write('\n')
    in_file.write(str(Count(c3, cc)))
    in_file.write('\n')

    in_file.write('\n')

    # 4
    Count(d4, dd)
    in_file.write("Fourth-----------------------\n")
    in_file.write(str(d4))
    in_file.write('\n')
    in_file.write(str(Count(d4, dd)))
    in_file.write('\n')

    in_file.write('\n')

    # 5
    Count(e5, ee)
    in_file.write("Fifth-----------------------\n")
    in_file.write(str(e5))
    in_file.write('\n')
    in_file.write(str(Count(e5, ee)))
    in_file.write('\n')

    in_file.write('\n')

    # 6
    Count(f6, ff)
    in_file.write("Sixth-----------------------\n")
    in_file.write(str(f6))
    in_file.write('\n')
    in_file.write(str(Count(f6, ff)))
    in_file.write('\n')
