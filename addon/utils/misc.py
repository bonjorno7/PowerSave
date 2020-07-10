import bpy


def purge_orphans():
    names = dir(bpy.data)
    collections = []

    for name in names:
        item = getattr(bpy.data, name, None)
        if isinstance(item, bpy.types.bpy_prop_collection):
            collections.append(item)

    purged = 0

    while True:
        before = sum(len(x) for x in collections)

        for collection in collections:
            for item in collection:
                if item.users == 0:
                    collection.remove(item)

        after = sum(len(x) for x in collections)

        if before > after:
            purged += before - after
        else:
            break

    return {'INFO'}, f'Deleted {purged} data-block(s)', {'FINISHED'}
