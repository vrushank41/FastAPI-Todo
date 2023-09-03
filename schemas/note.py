def noteEntity(items)->dict:
    return {
        "id":items["_id"],
        "title":items["title"],
        "description":items["description"],
        "status":items["status"]
    }

def notesEntity(items)->list:
    newDoc=[]
    for dat in items:
        newDoc.append(noteEntity(dat))
    return newDoc