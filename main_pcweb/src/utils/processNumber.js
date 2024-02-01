// 处理返回的文字内容
export function processNumber(numStr) {
  if (typeof numStr !== 'string') {
    numStr = String(numStr); // 将参数转换为字符串
  }

  // 判断是否为数字
  if (!isNaN(numStr) || !isNaN(numStr.replace('.', ''))) {
    // 处理小数点及小数部分
    if (numStr.includes('.')) {
      const [integerPart, decimalPart] = numStr.split('.');
      let processedDecimal;
      if (decimalPart.length === 2) {
        processedDecimal = decimalPart;
      } else {
        processedDecimal = decimalPart.padEnd(2, '0');
      }
      numStr = `${integerPart}.${processedDecimal}`;
    } else {
      // 处理不含小数点的情况
      numStr = `${numStr}.00`;
    }

    // 判断正负
    const isNegative = numStr.startsWith('-');
    if (isNegative) {
      numStr = numStr.slice(1); // 移除负号
    }

    // 处理整数部分逗号分隔
    if (numStr.length > 3) {
      const [integerPart, decimalPart] = numStr.split('.');
      let separatedInteger = integerPart;
      const reversedIntegerPart = separatedInteger.split('').reverse().join('');
      separatedInteger = reversedIntegerPart.match(/.{1,3}/g).join(',').split('').reverse().join('');
      numStr = `${separatedInteger}${decimalPart ? `.${decimalPart}` : ''}`;
    }

    if (isNegative) {
      numStr = `-${numStr}`; // 添加负号
    }
  }

  return numStr;
}