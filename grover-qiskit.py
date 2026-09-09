"""
Qiskitで実装するGrover探索｜「あたり」を高速に見つける

元記事: https://quantum.yurufuwa.work/learn/grover-qiskit
ゆるふわ量子コンピュータ (quantum.yurufuwa.work) の解説記事から抜粋したコードです。
"""

from qiskit import QuantumCircuit

def oracle_11():
    qc = QuantumCircuit(2, name="oracle")
    qc.cz(0, 1)      # |11⟩ にだけ -1 の位相をつける
    return qc

def diffuser(n):
    qc = QuantumCircuit(n, name="diffuser")
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n-1)
    qc.mcx(list(range(n-1)), n-1)   # 多制御X
    qc.h(n-1)
    qc.x(range(n))
    qc.h(range(n))
    return qc

from qiskit_aer import AerSimulator

n = 2
qc = QuantumCircuit(n, n)
qc.h(range(n))                       # 全部を重ね合わせ（一様な初期状態）

qc.compose(oracle_11(), inplace=True)
qc.compose(diffuser(n), inplace=True)

qc.measure(range(n), range(n))

result = AerSimulator().run(qc, shots=1000).result()
print(result.get_counts())
