from db.relational.dals import TG_DAL

path = "app/db/relational"
print(TG_DAL()._get_api_keys(path_to_file=path))