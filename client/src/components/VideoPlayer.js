import React, { useState, useEffect } from 'react';

const VideoPlayer = ({ rtspUrl }) => {
  const [video, setVideo] = useState(null);

  useEffect(() => {
    const videoElement = document.getElementById('video');
    if (videoElement) {
      videoElement.srcObject = new MediaStream();
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
          videoElement.srcObject = stream;
          setVideo(stream);
        })
        .catch(error => console.error(error));
    }
  }, []);

  const handlePlay = () => {
    if (video) {
      video.play();
    }
  };

  const handlePause = () => {
    if (video) {
      video.pause();
    }
  };

  return (
    <div>
      <video id="video" width="640" height="480" controls>
        <source src={rtspUrl} type="video/mp4" />
     