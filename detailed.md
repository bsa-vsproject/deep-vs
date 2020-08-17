
1- Download the PBB file of the protein of interest.
2- Convert the PDB into mol2 format using IChem as such 'IChem --noLig pdbconv 2le3.pdb output 2le3'.
3- Generate the cavities of the protein along with their description vectors using IChem as such 'IChem --desc volsite 2le3.mol2'.
4- Save the vectors in csv format as such 2le3_cavity_vectors.csv.
5- Use the 'python mlp_vscreen_predict.py -i cavity_vectors.csv -m mlp_vscreen_train_model.h5 -o predicted_lig.csv' code by adapting the code to your own file name. - This code predicts the ligands for the given protein cavity as a 300-dimensional vector format.
6- You will get 'predicted_lig.csv' file.
7- Use the 'python mlp_vscreen_library.py -i predicted_lig.csv -l 100k.csv' code by adapting to your own file. - This code screen the chemical molecule which contains 100 thousand molecules to find the most similar molecule to obtained one with cosine similarity function.
8- You will see the closest 5 ligands for your protein cavities and their cosine similarity values on the terminal screen.
