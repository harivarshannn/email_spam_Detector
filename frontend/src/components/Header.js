import React from 'react';
import { motion } from 'framer-motion';
import './Header.css';

const Header = () => {
  return (
    <motion.header 
      className="header"
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ type: "spring", stiffness: 100 }}
    >
      <div className="header-content">
        <motion.div 
          className="logo"
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
        >
          <span className="logo-icon">🛡️</span>
          <span className="logo-text">Email Spam Detector</span>
        </motion.div>
        
        <motion.div 
          className="header-subtitle"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.3 }}
        >
          Machine Learning-Powered Email Classifier
        </motion.div>

        <div className="header-stats">
          <motion.div 
            className="stat-item"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.4 }}
          >
            <div className="stat-value">98.79%</div>
            <div className="stat-label">Accuracy</div>
          </motion.div>
          <motion.div 
            className="stat-item"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.5 }}
          >
            <div className="stat-value">11K+</div>
            <div className="stat-label">Trained On</div>
          </motion.div>
          <motion.div 
            className="stat-item"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.6 }}
          >
            <div className="stat-value">3000</div>
            <div className="stat-label">Features</div>
          </motion.div>
        </div>
      </div>
    </motion.header>
  );
};

export default Header;
