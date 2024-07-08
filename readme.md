To open venv  : venv\Scripts\activate 

Open 2 of them and for each, execute :

- rasa run --enable-api --cors "*"  --log-file out.log --debug                                                      
                                                                                                             
- rasa run actions --debug  

to train more : rasa train 

web chat example : C:\Users\axelm\Projets\Chatbot-test\index.html

python -m pip install --force-reinstall absl-py==0.9  
ython -m pip install --force-reinstall absl-py=0.9  
> python -m pip install --force-reinstall absl-py>=0.9     
pip install --force-reinstall absl-py<0.10,>=0.9                             
                                                                                                              