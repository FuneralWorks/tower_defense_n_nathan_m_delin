import Animat


def create(nbMonster, horde, bg):
    level = dict()
    level["nbMonster"] = nbMonster
    level["horde"] = horde

    for i in range(0, level["nbMonster"] - 1):

        animat = Animat.create(
            direction="right",
            x=bg["spawn"][1],
            y=bg["spawn"][0],
            cara="M",
            finishx=bg["finish"][1],
            finishy=bg["finish"][0],
            color=1,
            life=4
        )
    level["horde"].append(animat)

    return level
