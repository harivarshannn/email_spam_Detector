import React from 'react';
import { motion } from 'framer-motion';
import { FiGithub, FiLinkedin, FiMail } from 'react-icons/fi';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <motion.div 
          className="footer-section"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
        >
          <h4>🛡️ Email Spam Detector</h4>
          <p>Machine Learning-powered email classification system built with Python, Flask, React, and Scikit-learn.</p>
        </motion.div>

        <motion.div 
          className="footer-section"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
        >
          <h4>Tech Stack</h4>
          <div className="tech-tags">
            <span className="tech-tag">Python</span>
            <span className="tech-tag">Flask</span>
            <span className="tech-tag">React</span>
            <span className="tech-tag">Scikit-learn</span>
            <span className="tech-tag">NLTK</span>
            <span className="tech-tag">TF-IDF</span>
          </div>
        </motion.div>

        <motion.div 
          className="footer-section"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
        >
          <h4>Model Performance</h4>
          <div className="performance-stats">
            <div className="stat">Accuracy: <strong>98.79%</strong></div>
            <div className="stat">Precision: <strong>94.16%</strong></div>
            <div className="stat">Recall: <strong>96.99%</strong></div>
          </div>
        </motion.div>

        <motion.div 
          className="footer-section"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.5 }}
        >
          <h4>Connect</h4>
          <div className="social-links">
            <a href="https://github.com" target="_blank" rel="noopener noreferrer" className="social-link">
              <FiGithub /> GitHub
            </a>
            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" className="social-link">
              <FiLinkedin /> LinkedIn
            </a>
            <a href="mailto:your.email@example.com" className="social-link">
              <FiMail /> Email
            </a>
          </div>
        </motion.div>
      </div>

      <div className="footer-bottom">
        <p>© 2024 Email Spam Detector. Built with ❤️ for Machine Learning Portfolio</p>
        <p className="footer-note">#MachineLearning #NLP #Python #DataScience #AI</p>
      </div>
    </footer>
  );
};

export default Footer;
