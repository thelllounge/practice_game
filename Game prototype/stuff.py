# create a way to randomize weapons in here.
# maybe this could be built into the encounters file actually, but I don't have time to do that now.

def create_encounter(creature, name_base, range_bottom, range_top):
    return [creature("dagger", f"{name_base} {i}") for i in range(range_bottom, range_top)]