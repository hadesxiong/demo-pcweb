// 处理日期迭代
import dayjs from 'dayjs';

export function iterateMonths(startDate,endDate,iterator) {
    const start = dayjs(startDate).startOf('month');
    const end = dayjs(endDate).endOf('month');

    let current = start.clone();
    while (current.isBefore(end) || current.isSame(end, 'month')) {
      iterator(current.endOf('month'));
      current = current.add(1, 'month').startOf('month');
    }
}