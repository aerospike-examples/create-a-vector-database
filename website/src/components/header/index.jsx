import styles from './index.module.css';

const Header = () => {
  return (
      <>
      <header className={styles.header}>
        <div className={styles.logo}>
          <img src="/CreaturesOfMythologyBankLogo.jpeg" alt="Bank logo"/>
          <div>
            <h3 className={styles.subHeading}>Welcome to the</h3>
            <h1>Creatures of Mythology Bank</h1>
          </div>
        </div>
      </header>
      </>
  )
}

export default Header;
