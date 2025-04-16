import { Module } from '@nestjs/common';

import { ProductModule } from './modules/product/product.module';
import { UserModule } from './modules/user/user.module';
import { OrderModule } from './modules/order/order.module';
import { OrderDetailModule } from './modules/order-detail/order-detail.module';
import { AccountModule } from './modules/account/account.module';
import { AdminModule } from './modules/admin/admin.module';

@Module({
  imports: [ProductModule, UserModule, OrderModule, OrderDetailModule, AccountModule, AdminModule],
})
export class AppModule {}
