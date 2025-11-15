import React from 'react';
import { motion } from 'framer-motion';
import { FiSend, FiTrash2 } from 'react-icons/fi';
import './InputSection.css';

const InputSection = ({ emailText, setEmailText, analyzeEmail, clearAll, error }) => {
  const handleKeyPress = (e) => {
    if (e.ctrlKey && e.key === 'Enter') {
      analyzeEmail();
    }
  };

  return (
    <motion.div 
      className="input-section"
      initial={{ opacity: 0, x: -50 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div className="section-header">
        <h2>📧 Enter Email or Message</h2>
        <p>Paste any email or text message to check if it's spam</p>
      </div>

      <textarea
        className="email-input"
        value={emailText}
        onChange={(e) => setEmailText(e.target.value)}
        onKeyDown={handleKeyPress}
        placeholder="Paste your email or message here...&#10;&#10;Try something like:&#10;'WINNER!! You've won $1000! Click here now!'&#10;or&#10;'Hey, can we meet for coffee tomorrow?'"
        rows="10"
      />

      {error && (
        <motion.div 
          className="error-message"
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
        >
          ⚠️ {error}
        </motion.div>
      )}

      <div className="button-group">
        <motion.button
          className="btn btn-primary"
          onClick={analyzeEmail}
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
        >
          <FiSend /> Analyze Email
        </motion.button>
        <motion.button
          className="btn btn-secondary"
          onClick={clearAll}
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
        >
          <FiTrash2 /> Clear
        </motion.button>
      </div>

      <div className="keyboard-hint">
        💡 Tip: Press <kbd>Ctrl</kbd> + <kbd>Enter</kbd> to analyze
      </div>
    </motion.div>
  );
};

export default InputSection;
