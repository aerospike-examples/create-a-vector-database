import styles from './index.module.css';
import Header from '../components/header';
import Conversation from '../components/conversation';
import Browser from '../components/browser';

const App = () => {
  return (
      <div className={styles.container}>
        <div className={styles.app}>
          <Header />
          <Conversation />
        </div>
        <div className={styles.browser}>
          <Browser />
        </div>
      </div>
  )
}

export default App
