kuukaudet = ('tammikuu', 'helmikuu', 'maaliskuu', 'huhtikuu', 'toukokuu', 'kesäkuu', 'heinäkuu', 'elokuu', 'syyskuu',
             'lokakuu', 'marraskuu', 'joulukuu')

jarjestys = int(input('Anna kuukauden numero (1-12): '))
kuukausi = kuukaudet[jarjestys-1]

if 0 <= kuukausi < 4:
    print('talvi')
elif 4<= kuukausi <7:
    print('kevät')
elif 7<= kuukausi <10:
    print('kesä')
elif 10<= kuukausi <0:
    print('syksy')

