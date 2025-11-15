import React from 'react';
import { motion } from 'framer-motion';
import { FiShield, FiAlertTriangle, FiCheckCircle } from 'react-icons/fi';
import './ResultCard.css';

const ResultCard = ({ result }) => {
  const isSpam = result.prediction === 'spam';
  
  return (
    <motion.div 
      className="result-card"
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.9 }}
      transition={{ duration: 0.4 }}
    >
      <div className="result-header">
        <motion.div 
          className={`result-badge ${isSpam ? 'spam' : 'ham'}`}
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.2, type: "spring", stiffness: 200 }}
        >
          {isSpam ? <FiAlertTriangle /> : <FiCheckCircle />}
          <span>{result.label}</span>
        </motion.div>
        
        <motion.div 
          className="confidence-badge"
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.3 }}
        >
          <FiShield />
          {result.confidence.toFixed(1)}% Confident
        </motion.div>
      </div>

      <div className="result-description">
        {isSpam ? (
          <p>⚠️ This message appears to be <strong>spam or a scam</strong>. Be cautious and avoid clicking any links or sharing personal information.</p>
        ) : (
          <p>✅ This message appears to be <strong>legitimate</strong>. However, always verify the sender before taking any action.</p>
        )}
      </div>

      <div className="probability-section">
        <h3>Probability Analysis</h3>
        
        <div className="prob-item">
          <div className="prob-header">
            <span className="prob-label">
              <span className="prob-icon legitimate">✓</span>
              Legitimate
            </span>
            <span className="prob-value">{result.ham_probability.toFixed(2)}%</span>
          </div>
          <div className="prob-bar-container">
            <motion.div 
              className="prob-bar legitimate"
              initial={{ width: 0 }}
              animate={{ width: `${result.ham_probability}%` }}
              transition={{ duration: 1, delay: 0.4 }}
            />
          </div>
        </div>

        <div className="prob-item">
          <div className="prob-header">
            <span className="prob-label">
              <span className="prob-icon spam">⚠</span>
              Spam/Scam
            </span>
            <span className="prob-value">{result.spam_probability.toFixed(2)}%</span>
          </div>
          <div className="prob-bar-container">
            <motion.div 
              className="prob-bar spam"
              initial={{ width: 0 }}
              animate={{ width: `${result.spam_probability}%` }}
              transition={{ duration: 1, delay: 0.5 }}
            />
          </div>
        </div>
      </div>

      <div className="processed-section">
        <h4>🔍 Processed Text</h4>
        <div className="processed-text">
          {result.cleaned_text || 'N/A'}
        </div>
        <p className="processed-note">
          This is the cleaned text after removing URLs, numbers, special characters, and stopwords.
        </p>
      </div>

      <div className="model-info">
        <div className="info-item">
          <span className="info-label">Model:</span>
          <span className="info-value">Logistic Regression</span>
        </div>
        <div className="info-item">
          <span className="info-label">Features:</span>
          <span className="info-value">TF-IDF (3000)</span>
        </div>
        <div className="info-item">
          <span className="info-label">Accuracy:</span>
          <span className="info-value">98.79%</span>
        </div>
      </div>
    </motion.div>
  );
};

export default ResultCard;
