"""convert coefficents from Ryckaert-Bellemans to oplsaa for dihedrals"""

def conversion(
               l_rb: list[float]  # RB coefficint
               ) -> list[float]:  # Oplsaa parameters
    """convert the coeffs"""
    if len(l_rb) > 4:
        print(f'\nWarning! More then 4 rb coeffs, only first 4 is selected')
    elif len(l_rb) > 4:
        exit(f'Error! Not enough parameters\n')
    l_opls: list[float] = [0 for _ in range(4)]  # opls converted list
    l_opls[0] = -2*l_rb[1]-(3/2.)*l_rb[3]
    l_opls[1] = l_rb[0] + l_rb[1] + l_rb[3]
    l_opls[2] = -l_rb[3]/2
    l_opls[3] = (l_rb[0] + l_rb[1] + l_rb[2] + l_rb[3])/4
    l_opls = [item/4.184 for item in l_opls]
    return l_opls

CTCTCTCT = [2.92880, -1.46440, 0.20920, -1.67360, 0.00000, 0.00000]
CTCTCTNT = [3.33465, -1.55226, 2.82001, -4.60240, 0.00000, 0.00000]
CTCTCTHC = [0.62760, 1.88280, 0.00000, -2.51040, 0.00000, 0.00000]
CTCTNTH = [-1.26775, 3.02085, 1.74473, -3.49782, 0.00000, 0.00000]
CTNTCTHC = [1.17152, 3.51456, 0.00000, -4.68608, 0.00000, 0.00000]
HCCTCTHC = [0.62760, 1.88280, 0.00000, -2.51040, 0.00000, 0.00000]
HNTCTHC = [0.83680, 2.51040, 0.00000, -3.34720, 0.00000, 0.00000]
CTCTNTCT = [1.78866,3.49154,0.53555,-5.81576,0.00000,0.00000]
HCCTCTNT = [-4.09614, 5.08775, 2.96645, -3.95806, 0.00000, 0.00000]

all_list = [CTCTCTCT, CTCTCTNT, CTCTCTHC, CTCTNTH, HCCTCTNT, HCCTCTHC,
            HNTCTHC, CTCTNTCT, CTNTCTHC]
for i, l in enumerate(all_list):
    ll = conversion(l)
    print(i+1, f'"k1": {ll[0]:5.3f}, "k2": {ll[1]:5.3f},'
          f'"k3": {ll[2]:5.3f},"k4": {ll[3]:5.3f}')


    5.4392, -0.20920000000000005, 0.8368, 0.0