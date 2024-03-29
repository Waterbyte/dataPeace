from flask import g
from pymongo import MongoClient as mc


def get_db_client():
    if 'dbcl' not in g:
        g.dbcl = mc('mongodb://10.131.65.27:27017/')
    return g.dbcl


def get_db():
    return get_db_client()['datapeace']


def get_collection(coll_name=None):
    if coll_name is not None:
        return get_db()[coll_name]
    else:
        return None


def close_dbcl(e=None):
    dbcl = g.pop('dbcl', None)
    if dbcl is not None:
        dbcl.close()


def init_app(app):
    app.teardown_appcontext(close_dbcl)


def count_doc(coll, argsDict):
    cln = get_collection(coll)
    return cln.count_documents(argsDict)


def insert_one_doc(coll, doc):
    cln = get_collection(coll)
    res = cln.insert_one(doc)
    return res


def create_index(coll, expr, uniqueKey):
    cln = get_collection(coll)
    cln.create_index(expr, unique=uniqueKey)


def upsert_one(coll, filt, updt):
    cln = get_collection(coll)
    return cln.update_one(filt, updt,
                          upsert=True).modified_count  # this will contain the number of modified docs, monitor its behaviour


def del_docs(coll, filter):
    cln = get_collection(coll)
    return cln.delete_many(filter).deleted_count  # returns number of deleted docs


def find_docs_count(coll, expr):
    return find_docs(coll, expr).count()


def find_docs(coll, expr):
    cln = get_collection(coll)
    return cln.find(expr)


def find_single_doc_with_desc_sort(coll, expr, proj, sortExpr):
    cln = get_collection(coll)
    return cln.find(expr, proj).sort(sortExpr).limit(1)


def find_docs_projection(coll, expr, proj):
    cln = get_collection(coll)
    return cln.find(expr, proj)


def edit_single_doc(coll, filter, update):
    cln = get_collection(coll)
    return cln.update_one(filter, update).modified_count  # will return number of documents updated


def find_and_modify(coll, expr, updt, wantNew):
    cln = get_collection(coll)
    return cln.find_one_and_update(expr, updt, wantNew)


def aggregate_db(coll, expr):
    cln = get_collection(coll)
    return cln.aggregate(expr)


def delete_one(coll, expr):
    cln = get_collection(coll)
    return cln.delete_one(expr)
