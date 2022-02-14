import streamlit as st
from detector import *
#detector = Detector(model_type='keypointsDetection')

#detector.onVideo("pexels-tima-miroshnichenko-6388396.mp4")
#@st.cache
def func_1(x):
    detector = Detector(model_type=x)
    image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
    if image_file is not None:
        file_details = {"FileName":image_file.name,"FileType":image_file.type}
        st.write(file_details)
        img = Image.open(image_file)
        st.image(img, caption='Uploaded Image.')
        with open(image_file.name,mode = "wb") as f: 
            f.write(image_file.getbuffer())         
        st.success("Saved File")
        detector.onImage(image_file.name)
        img_ = Image.open("result.jpg")
        st.image(img_, caption='Proccesed Image.')

def func_2(x):
    detector = Detector(model_type=x)
    uploaded_video = st.file_uploader("Upload Video", type = ['mp4','mpeg','mov'])
    if uploaded_video != None:
        
        vid = uploaded_video.name
        with open(vid, mode='wb') as f:
            f.write(uploaded_video.read()) # save video to disk
    
        st_video = open(vid,'rb')
        video_bytes = st_video.read()
        st.video(video_bytes)
        st.write("Uploaded Video")
        detector.onVideo(vid)
        st_video = open('output.mp4','rb')
        video_bytes = st_video.read()
        st.video(video_bytes)
        st.write("Detected Video") 




def main():
    with st.expander("About the App"):
        st.markdown( '<p style="font-size: 30px;"><strong>Welcome to my Object Detection App!</strong></p>', unsafe_allow_html= True)
        st.markdown('<p style = "font-size : 20px; color : white;">This app was built using Streamlit, Detectron2 and OpenCv to demonstrate <strong>Object Detection</strong> and its variants like <em> Keypoint Detection, Instance Segmentation</em> in both videos (pre-recorded) and images.</p>', unsafe_allow_html=True)

    #st.sidebar.title("Select Activity")
    #st.sidebar.markdown("MODE")
    #choice  = st.sidebar.selectbox("MODE",("About","Image","Video"))
    #about = st.sidebar.selectbox("About" ,["About"] ,index = 0,help='What this app is about!')
    #img = st.sidebar.selectbox("Image",['imgObjectDetection',"imgInstanceSegmentation",'imgKeypointsDetection'], index = 0,help= 'Choose which activity you want to take place')
    
    #vid = st.sidebar.selectbox("Video",['vidObjectDetection',"vidInstanceSegmentation",'vidKeypointsDetection'], index = 0,help= 'Choose which activity you want to take place')


    option = st.selectbox(
     'What Type of File do you want to work with?',
     ('Images', 'Videos'))

    #st.write('You selected:', option)
    if option == "Images":
        option_1 = st.selectbox(
     'What Type of Detection Should be Performed on this Image?',
     ('ObjectDetection',"InstanceSegmentation",'KeypointsDetection'))
        #st.write('You selected:', option_1)
        if option_1 == 'ObjectDetection':
            st.title('Object Detection for Images')
            st.subheader("""
    This takes in an image and outputs the image with bounding boxes created around the objects in the image.
    """)
            func_1('objectDetection')
        elif option_1 == "InstanceSegmentation":
            st.title('Instance Segmentation for Images')
            st.subheader("""
    This takes in an image and outputs the image ,providing the exact outline of objects within the image.
    """)
            func_1('instanceSegmentation')
        elif option_1 == "KeypointsDetection":
            st.title('Keypoint Detection for Images')
            st.subheader("""
    This takes in an image and outputs the image, locating key object parts such as the nosetips, eye corners, eyebrows e.t.c within the image.
    """)
            func_1('keypointsDetection')
    
    elif option == "Videos":
        option_2 = st.selectbox(
     'What Type of Detection Should be Performed on this Video?',
     ('ObjectDetection',"InstanceSegmentation",'KeypointsDetection'))
        if option_2 == 'ObjectDetection':
            st.title('Object Detection for Videos')
            st.subheader("""
    This takes in a video and outputs the video with bounding boxes created around the objects in the video.
    """)
            func_2('objectDetection')
        elif option_2 == "InstanceSegmentation":
            st.title('Instance Segmentation for Videos')
            st.subheader("""
    This takes in a video and outputs the video ,providing the exact outline of objects within the video.
    """)
            func_2('instanceSegmentation')

        elif option_2 == 'KeypointsDetection':
            st.title('Keypoint Detection for Videos')
            st.subheader("""
    This takes in a video and outputs the video, locating key object parts such as the nosetips, eye corners, eyebrows e.t.c within the video.
    """)
            func_2('keypointsDetection')





    

if __name__ == '__main__':
		main()	
