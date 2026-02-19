import os
import random
import shutil
from parser import extract_metadata # We reuse your logic!

def perform_stratified_split(source_dir, train_dir, test_dir):
    # 1. Create folders if they don't exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # 2. Group files by age
    age_groups = {}
    files = [f for f in os.listdir(source_dir) if f.endswith('.txt')]
    
    for f in files:
        age = extract_metadata(f)
        if age is not None:
            if age not in age_groups:
                age_groups[age] = []
            age_groups[age].append(f)

    # 3. Perform the split (3 for test, 27 for train per age)
    for age, age_files in age_groups.items():
        random.shuffle(age_files) # Randomize which texts are picked
        test_files = age_files[:3]
        train_files = age_files[3:]

        # Move to respective folders
        for f in test_files:
            shutil.copy(os.path.join(source_dir, f), os.path.join(test_dir, f))
        for f in train_files:
            shutil.copy(os.path.join(source_dir, f), os.path.join(train_dir, f))

    print(f"Split complete: {len(os.listdir(train_dir))} training files, {len(os.listdir(test_dir))} test files.")

if __name__ == "__main__":
    perform_stratified_split("corpus_age_etudiant/", "data/train/", "data/test/")