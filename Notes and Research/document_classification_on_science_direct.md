To quantify/evaluate results, spam is defined as positive and non-spam is defined as negative. Normal binary classification metrics (True Positive, True Negative, False Positive,and  False Negative) are used to evaluate the model’s predictions. Some big problems are balancing TPR and FPR (finding best location on ROC curve). Too far one way and the model will allow in too many spam emails; too far the other way and the model will flag normal emails as spam. Speed is also critical: there is a massive volume of emails that need to be processed. 


Data Set Stats:
        Size: 19,620 emails (not including spam)
        Number of Contacts: 2400
        Distinct Terms: 303,381
Once emails are collected, they are first converted to text files then compiled into a dataset. Words are stemmed, and those with a frequency above 100 are put in a frequency table. Emails are clustered, and names are applied to these clusters to avoid manually labeling emails with classes. Class definitions proposed are Personal, Job, Profession, Friendship, and Others. 


The Vector Space Model is used to allow classical clustering models to be applied (k-means, spherical k-means, etc.). Vectors are generated using a word-email matrix in which for each high frequency word in the matrix, index (word-num, email-num) is 1 if the word is in the email, and if not 0. The matrix can also be reversed. An alternative matrix is built storing the frequency of word occurrences in each email, not just a binary (yes/no) value. 


Elementary clustering as described below is performed in order to save time in initial clustering: 
        Pick a random document as a seed from the collection
        Evaluate how similar the document is to all other documents 
        Save the 100 closest emails as the cluster for the seed document
        Repeat for multiple seed documents


Two methods are evaluated and compared: Term Frequency and WordNet. 


In term frequency k-means was used to compare distances between vectors and cluster them accordingly. 


Inverse Document Frequency = log(N/n) where N = total number of documents and n = number of documents containing the keyword we are looking at.


K-Means was used to group the documents into clusters of 150 documents. 




Wordnet is a database that groups similar words into symptoms. A metric for gauging similarity between email content and body is constructed using a 2d matrix comparing all emails. This comparison is a value between 0 and 1. Relational K-means is used to cluster the emails using this matrix. 


3 SVM models are each used to classify emails into 3 classes: 


Top 100 words vs emails before removing stop words
        100% TP, high FP because library didn’t process arabic words well


top 100 words vs emails after removing stop words
        100% TP, lower FP


NGram terms vs emails
        Slightly less than 100% TP, drastically lower FP.
