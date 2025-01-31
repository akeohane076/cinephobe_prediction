from model_class.model import Model

from data.data_cleaning_functions import load_data
from data.data_class import Data

# from data.constants import csv_file_path

csv_file_path = 'data/data_raw.csv'
rp = 'data/repeat_off.csv'

def main():
    rd = load_data(csv_file_path)
    rd1 = load_data(rp)
    D = Data(rd, rd1)
    D.add_actors()

    # print(D.data.head())
    D.split_data()

    D.make_feature_options()

    # print(D.a_data["Cast / Crew"])

    M = Model(D, 'Zach')
    M1 = Model(D, 'Amin')
    M2 = Model(D, 'Mayes')

    M.get_svc()
    M1.get_svc()
    M2.get_svc()

    # M.get_svc()

    # print(M.opt_dt_results)

    # M.get_kbest()
    # M1.get_kbest()
    # M2.get_kbest()

    # M.opt_log_reg()
    # M1.opt_log_reg()
    # M2.opt_log_reg()

    # M.get_svc()
    # M1.get_svc()
    # M2.get_svc()

    # print(M.opt_log_reg_score)
    # print(M1.opt_log_reg_score)
    # print(M2.opt_log_reg_score)

    # print(M.k_best_score)
    # print(M1.k_best_score)
    # print(M2.k_best_score)

    # print(M.best)
    # print(M.best_f)

    # print(M1.best)
    # print(M1.best_f)
    # print(M2.best)
    # print(M2.best_f)

main()