# Project in molecular Life science (KB8024/KB8025)
This contains my project for the course.

Clone the whole repository with all the files, for codes to work.

For my Final predictors-They are saved in the codes directory under the name "SVC_predictor.py" for the normla SVC model and as "SVC_predictor.py" for the PSSM predictor.

The "SVC_predictor.py" is predicting for 50unknownproteins in my datasets directory (hence takes a bit of time, please be patient), while the "SVC_predictor.py" is predicting for a single sequence given as pssm_test in my datasets.

For the "SVC_predictor.py", the model "PSSM_models.py" is trained on pssm_train file given in datasets. ALl the fasta and PSSM files for training sequences is in fasta_data while for the test sequence these files are in fastaoutput.

The predicted texts for the same are in directory Predicted texts saved as "SVC_predicted.txt" and for the PSSM_SVC model it is "PSSM_SVC_results"


