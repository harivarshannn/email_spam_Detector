import React from 'react';
import { motion } from 'framer-motion';
import { FiMail } from 'react-icons/fi';
import './SampleEmails.css';

const samples = [
  {
    id: 1,
    type: 'spam',
    title: 'Prize Winner Scam',
    text: "WINNER!! Congratulations! You have been selected to receive a $1000 Walmart gift card. Click here now to claim your prize: http://fake-link.com. This offer expires in 24 hours! Act fast!"
  },
  {
    id: 2,
    type: 'spam',
    title: 'Phishing Attack',
    text: "URGENT: Your bank account has been compromised! Click this link immediately to verify your identity and prevent account closure: http://phishing-site.com. Call 1-800-SCAM-NOW for assistance."
  },
  {
    id: 3,
    type: 'ham',
    title: 'Business Meeting',
    text: "Hi John, Thanks for your email yesterday. I've reviewed the project proposal and it looks great. Let's schedule a meeting next Tuesday at 2pm to discuss the next steps. Looking forward to working with you!"
  },
  {
    id: 4,
    type: 'ham',
    title: 'Dinner Plans',
    text: "Hey! Just wanted to remind you about dinner tonight at 7pm. I made a reservation at that Italian restaurant you mentioned. See you there! Let me know if you're running late."
  },
  {
    id: 5,
    type: 'spam',
    title: 'Lottery Scam',
    text: "You've WON £500,000 in the UK National Lottery! To claim your prize, send your bank details to lottery@scam.com. Reply within 48 hours or forfeit your winnings!"
  },
  {
    id: 6,
    type: 'ham',
    title: 'Work Update',
    text: "Hi team, Just a quick update on the project timeline. We're on track to meet the deadline next Friday. Please submit your final reports by Wednesday. Thanks for all your hard work!"
  }
];

const SampleEmails = ({ loadSample }) => {
  return (
    <motion.div 
      className="sample-emails"
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: 0.2 }}
    >
      <div className="sample-header">
        <h3>📬 Try Sample Emails</h3>
        <p>Click any sample to test the detector</p>
      </div>

      <div className="samples-grid">
        {samples.map((sample, index) => (
          <motion.div
            key={sample.id}
            className={`sample-card ${sample.type}`}
            onClick={() => loadSample(sample.text)}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 * index }}
            whileHover={{ scale: 1.02, y: -5 }}
            whileTap={{ scale: 0.98 }}
          >
            <div className="sample-icon">
              <FiMail />
            </div>
            <div className="sample-content">
              <div className="sample-title">{sample.title}</div>
              <div className="sample-preview">{sample.text.substring(0, 80)}...</div>
              <div className={`sample-badge ${sample.type}`}>
                {sample.type === 'spam' ? '⚠️ Spam' : '✓ Legitimate'}
              </div>
            </div>
          </motion.div>
        ))}
      </div>
    </motion.div>
  );
};

export default SampleEmails;
