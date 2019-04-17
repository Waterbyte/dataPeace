import pymongo

from backendAPI import db, constants


def createUsers(args):
    try:
        db.insert_one_doc(constants.CollectionName.users.name, args)
        return True
    except:
        return False


def getUser(id):
    data = {}
    try:
        expr = {constants.UserEntry.id.name: id}
        projection = {"_id": 0}
        cursor = db.find_docs_projection(constants.CollectionName.users.name, expr, projection)
        for val in cursor:
            data = val
        return data
    except Exception as e:
        print(e)
        return data


def deleteUser(id):
    try:
        expr = {constants.UserEntry.id.name: id}
        db.delete_one(constants.CollectionName.users.name, expr)
        return True
    except:
        return False


def modifyUser(args, id):
    try:
        expr = {constants.UserEntry.id.name: id}
        updt = {'$set': args}
        db.find_and_modify(constants.CollectionName.users.name, expr, updt, {})
        return True
    except:
        return False


def getUsersWithParams(args):
    resultList = []
    expr = {}
    sortExpr = [("$natural", pymongo.ASCENDING)]
    skipNum = 0
    projection = {"_id": 0}
    limitParam = args["limit"]
    print(args)
    if "page" in args:
        skipNum = (args["page"]-1) * limitParam  #page starts from 1

    if "name" in args:
        reg = args["name"]
        expr = {'$or':[{constants.UserEntry.first_name.name:{"$regex":reg}},{constants.UserEntry.last_name.name:{"$regex":reg}}]}

    if "Sort" in args:
        Sort = args["Sort"]
        if Sort.startswith("-"):
            sortExpr = [(Sort[1:], pymongo.DESCENDING)]
        else:
            sortExpr = [(Sort, pymongo.ASCENDING)]

    print(sortExpr)
    print(expr)

    try:
        cursor = db.find_docs_projection(constants.CollectionName.users.name, expr, projection).limit(limitParam).skip(skipNum).sort(sortExpr)
        for val in cursor:
            resultList.append(val)
    except Exception as e:
        print(e)
    return resultList
