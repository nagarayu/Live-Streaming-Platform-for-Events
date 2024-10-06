import React from 'react';

const Overlay = ({ overlay, handleDelete, handleUpdate }) => {
  return (
    <div>
      <h2>{overlay.name}</h2>
      <p>{overlay.content}</p>
      <button onClick={() => handleDelete(overlay.id)}>Delete</button>
      <button onClick={() => handleUpdate(overlay.id)}>Update</button>
    </div>
  );
};

export default Overlay;