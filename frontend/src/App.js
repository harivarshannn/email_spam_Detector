import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import axios from 'axios';
import './App.css';
import Header from './components/Header';
import InputSection from './components/InputSection';
import ResultCard from './components/ResultCard';
import SampleEmails from './components/SampleEmails';
import Footer from './components/Footer';
import LoadingSpinner from './components/LoadingSpinner';

function App() {
  const [emailText, setEmailText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const analyzeEmail = async () => {
    if (!emailText.trim()) {
      setError('Please enter some text to analyze!');
      return;
    }

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await axios.post('/predict', {
        text: emailText
      });
      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'Error connecting to server');
    } finally {
      setLoading(false);
    }
  };

  const clearAll = () => {
    setEmailText('');
    setResult(null);
    setError('');
  };

  const loadSample = (sampleText) => {
    setEmailText(sampleText);
    setResult(null);
    setError('');
  };

  return (
    <div className="App">
      <Header />
      
      <motion.div 
        className="container"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <div className="main-grid">
          <div className="left-section">
            <InputSection
              emailText={emailText}
              setEmailText={setEmailText}
              analyzeEmail={analyzeEmail}
              clearAll={clearAll}
              error={error}
            />
            <SampleEmails loadSample={loadSample} />
          </div>

          <div className="right-section">
            <AnimatePresence mode="wait">
              {loading && <LoadingSpinner key="loading" />}
              {result && !loading && <ResultCard key="result" result={result} />}
              {!result && !loading && (
                <motion.div
                  key="placeholder"
                  className="placeholder-card"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                >
                  <div className="placeholder-icon">🔍</div>
                  <h3>Ready to Analyze</h3>
                  <p>Enter an email or message on the left and click "Analyze" to detect spam</p>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        </div>
      </motion.div>

      <Footer />
    </div>
  );
}

export default App;
