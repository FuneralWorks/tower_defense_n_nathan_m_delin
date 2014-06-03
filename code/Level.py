import Animat


def create(nbMonster, horde, bg, nbLevel):
    level = dict()
    level["nbMonster"] = nbMonster
    level["horde"] = horde
    level['nbLevel'] = nbLevel

    for i in range(0, level["nbMonster"] - 1):

        animat = Animat.create(
            direction="right",
            x=bg["spawn"][1],
            y=bg["spawn"][0],
            cara="M",
            finishx=bg["finish"][1],
            finishy=bg["finish"][0],
            color=1,
            life=4,
            mvt=False
        )
        level["horde"].append(animat)

    return level
