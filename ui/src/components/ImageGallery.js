import React from 'react';

function ImageGallery({ images }) {
  return (
    <div className="image-gallery">
      {images.map((img, index) => (
        <img key={index} src={img.src} alt={img.alt} />
      ))}
    </div>
  );
}

export default ImageGallery;
