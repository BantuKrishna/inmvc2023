import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                        format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)

        # logger.info("Logger initialized successfully.")
        # logger.info("Current logger level: %s", logging.getLevelName(logger.getEffectiveLevel()))
        return logger
