import Webcam from "react-webcam";
import Axios from 'axios'
import { useCallback, useRef, useState } from "react";
import './index.css';

function ImageCollection() {
    const [emotion, setEmotion] = useState("");
    const camInstance = useRef(null);


    const capture = useCallback( async () => {
        const imageSrc = camInstance.current.getScreenshot();
        let receivedResponse = true;
        const response = await Axios.post('http://127.0.0.1:8000/send/', {
                'data': imageSrc
        })
        .catch((error) => {
            setEmotion("ERROR: API is not running");
            console.log(error);
            receivedResponse = false;
          });
        if(receivedResponse) {
            console.log(response.data);
            setEmotion(response.data);
        }
    }, []);
    return (
        <div className="container">
            <center>
                <Webcam height={window.innerHeight * 0.6} width={window.innerWidth * 0.6} ref={camInstance} screenshotFormat='image/jpg'/><br />
                <button className="emotion-button" onClick={capture}>Predict Emotion</button><br />
                <h1>{emotion}</h1>
            </center>
        </div>
    )
}

export default ImageCollection;