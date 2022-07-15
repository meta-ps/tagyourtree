require("@nomiclabs/hardhat-waffle");

require("dotenv").config();



module.exports = {
  networks: {
    hardhat: {
      chainId: 1337,
    },
    mumbai: {
      // url: "https://mainnet.infura.io/v3/46c3d79839ba45fcbaf9d54c0a80d231",
      // url: "https://rpc-mumbai.matic.today",
      url: "https://polygon-mumbai.g.alchemy.com/v2/L-yGAmmX596J4TuHNzcNwLpIDC_dYquy",
      accounts: ["ce8c7c7b30f2ee6cf872e583955232a814f7cca1075576a0968a706fa913c75b"]
    }
  },
  solidity: {
    version: "0.8.1",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  paths: {
    sources: "./contracts",
    tests: "./test",
    cache: "./contracts/cache",
    artifacts: "./contracts/artifacts"
  },
  mocha: {
    timeout: 40000
  }
}


