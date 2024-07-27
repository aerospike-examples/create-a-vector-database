import styles from './index.module.css';

const Header = () => {
  return (
      <>
      <div className={styles.stripe}/>
      <header className={styles.header}>
        <a className={styles.aerospike} href='/'><img src="/Aerospike_Logo_Space_Blue_RGB.png" alt="Aerospike logo"/></a>
      </header>
      <div className={styles.logo}>
        <img src="/CreaturesOfMythologyBankLogo.jpeg" alt="Bank logo"/>
        <div>
          <h3>Welcome to the</h3>
          <h1>Creatures of Mythology Bank</h1>
        </div>
      </div>
      </>
  )
}

export default Header;
