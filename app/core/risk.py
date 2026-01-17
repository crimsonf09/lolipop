class RiskManager:
    def evaluate(self, signal, price, position, cash):
        return {
            "allow_trade": True,
            "size": 1
        }
