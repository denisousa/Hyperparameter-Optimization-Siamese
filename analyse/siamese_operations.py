import pandas as pd
from pprint import pprint
import random

def remove_absolute_path(path):
    return path.split('my_index')[-1].split('#')[0].split('.java')[0] + '.java'

def get_numbers_from_absolute_path(path):
    return int(path.split("#")[-2]), int(path.split("#")[-1])

def get_method_name(path):
    return path.split('my_index')[-1].split('#')[0].split('.java')[-1][1:]

def format_clones(search_clone, clone):    
    clean_path1 = remove_absolute_path(search_clone)
    start1, end1 = get_numbers_from_absolute_path(search_clone)
    method1 = get_method_name(search_clone)
        
    clean_path2 = remove_absolute_path(clone)
    start2, end2 = get_numbers_from_absolute_path(clone)

    return {
        "file1": clean_path1,
        "start1": start1,
        "end1": end1,
        "method1": method1,
        "file2": clean_path2,
        "start2": start2,
        "end2": end2,
    }

def show_clone_by_index(df, index):
    line = df.loc[index]
    path1, path2 = line['file1'], line['file2']
    
    path1, path2 = open(f'{my_index_path}{path1}','r').read(), open(f'{my_index_path}{path2}','r').read()
    path1, path2 = path1.split('\n')[line['start1']-1:line['end1']+1], path2.split('\n')[line['start2']-1:line['end2']+1]
    pprint(path1)
    print('\n\n')
    pprint(path2)

def show_clone_between(df_siamese_clones, start, end):
    # Incomplete
    for index, row in df.iterrows():
        pass
    
def execute_siamese(project):
    os.system(f'cd Siamese-main && java -jar siamese-0.0.6-SNAPSHOT.jar -c search -i ./my_index/{project}/ -o ./output -cf config.properties')


def get_recall_precision_f1_score(X, Y):
    return random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)

def main():
    output_path = '/home/denis/Hyperparameter-Optimization-Siamese/Siamese-main/output'
    my_index_path = '/home/denis/Hyperparameter-Optimization-Siamese/Siamese-main/my_index'

    siamese_clones = []
    df_qualitas_and_so = pd.read_csv('clones.csv')
    csv_lines = [line for line in open(f'{output_path}/stackoverflow_formatted_qr_02-05-23_05-06-550.csv', 'r').read().rstrip().split('\n')]

    for line in csv_lines:
        search_clone, indexed_clones = line.split(',')[0], line.split(',')[1:]
        [siamese_clones.append(format_clones(search_clone, clone)) for clone in indexed_clones]

    df_siamese_clones = pd.DataFrame(data=siamese_clones)
    print(df_qualitas_and_so.head())
    print(df_siamese_clones.head())

    df_siamese_clones.to_csv('df_siamese_clones.csv', encoding='utf-8')
    show_clone_by_index(df_siamese_clones, 0)
    grid_search()
