# Face-detection-web-app-
create Face detection web based app in local host

Our app will have a drag and drop/file upload section for uploading our images using the st.file_uploader function of Streamlit.
The image uploaded will be opened with python pillow package as well as with numpy to convert them into numpy arrays for the next section.
We will then create individual function to process and manipulate our images using pillow and opencv.

open command terminal and type: streamlit run app.py
This will open up the application in a web browser and you can run the app.
1. preprocessing the images:
            first we will convert captured images into GRAY from RGB to detect images and send them to Multiclassifier and crop them with slicing to improve fast execution
  
2.  Training:
            from dataset folder those images are send to LBPHFaceRecognizer to recognize then we will get name from path by spliting path and append those faces and id in                     repective lists.we will save our model in yml file to use it again.



3.Deployment:
             we will deploy our trained model using streamlit framework.
