import React, { useState, useEffect } from 'react';

const DreamForm = ({ onSubmit, dreamData }) => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [errors, setErrors] = useState({});
  const [globalError, setGlobalError] = useState('');

  useEffect(() => {
    try {
      if (dreamData) {
        setTitle(dreamData.title || '');
        setContent(dreamData.content || '');
      }
    } catch (error) {
      console.error("An error occurred while setting dream data: ", error);
      setGlobalError("Failed to load dream data.");
    }
  }, [dreamData]);

  const validateForm = () => {
    const errors = {};
    setGlobalError(''); // Reset global error state before validation
    
    if (!title.trim()) errors.title = "Title is required";
    if (!content.trim()) errors.content = "Content is required";
    setErrors(errors);
    
    return Object.keys(errors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!validateForm()) return;
    
    try {
      // Assuming onSubmit might be asynchronous. If it's not, you can remove `async` and `await`.
      await onSubmit({ title, content });
    } catch (error) {
      console.error("An error occurred during form submission: ", error);
      setGlobalError("Failed to submit dream data. Please try again.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {globalError && <div className="global-error">{globalError}</div>}
      <div>
        <label htmlFor="title">Title</label>
        <input
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          type="text"
          className={errors.title ? 'error' : ''}
        />
        {errors.title && <div className="form-error">{errors.title}</div>}
      </div>
      <div>
        <label htmlFor="content">Content</label>
        <textarea
          id="content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          className={errors.content ? 'error' : ''}
        ></textarea>
        {errors.content && <div className="form-error">{errors.content}</div>}
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default DreamForm;