import React, { useState, useEffect } from 'react';

const DreamForm = ({ onSubmit, dreamData }) => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (dreamData) {
      setTitle(dreamData.title || '');
      setContent(dreamData.content || '');
    }
  }, [dreamData]);

  const validateForm = () => {
    const errors = {};
    if (!title) errors.title = "Title is required";
    if (!content) errors.content = "Content is required";
    setErrors(errors);
    return Object.keys(errors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!validateForm()) return;
    onSubmit({ title, content });
  };

  return (
    <form onSubmit={handleSubmit}>
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