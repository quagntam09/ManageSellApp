import { Injectable, BadRequestException, InternalServerErrorException, NotFoundException, Logger } from '@nestjs/common';
import { CreateShipperDto } from './dto/create-shipper.dto';
import { PrismaService } from '../prisma/prisma.service';
import { roles } from '../../configs/config.json';
import { CreateAccountDto } from '../account/dto/create-account.dto';
import { AccountService } from '../account/account.service';
import { UpdateShipperDto } from './dto/update-shipper.dto';

@Injectable()
export class ShipperService {
  private readonly logger = new Logger(ShipperService.name);

  constructor(
    private readonly prisma: PrismaService,
    private readonly accountservice: AccountService
  ) {}

 

  async getShipperById(id: string) {
    try {
      const shipper = await this.prisma.shipper.findUnique({ where: { id } });
      if (!shipper) {
        throw new NotFoundException('Không tìm thấy shipper');
      }
      return shipper;
    } catch (error) {
      this.logger.error(`Lỗi khi lấy shipper theo id=${id}`, error.stack);
      throw new InternalServerErrorException(error.message || 'Lỗi khi lấy shipper');
    }
  }

  async getAllShipper() {
    try {
      return await this.prisma.shipper.findMany();
    } catch (error) {
      this.logger.error('Lỗi khi lấy danh sách shipper', error.stack);
      throw new InternalServerErrorException('Lỗi khi lấy danh sách shipper');
    }
  }

  async uppdateShipper(id: string, data: UpdateShipperDto) {
    try {
      if (!data || Object.keys(data).length === 0) {
        throw new BadRequestException('Không có dữ liệu cập nhật được gửi lên');
      }
      const exist = await this.prisma.shipper.findUnique({ where: { id } });
      if (!exist) {
        throw new NotFoundException('Shipper không tồn tại');
      }

      return await this.prisma.shipper.update({ where: { id }, data });
    } catch (error) {
      this.logger.error(`Lỗi khi cập nhật shipper id=${id}`, error.stack);
      throw new InternalServerErrorException(error.message || 'Lỗi khi cập nhật shipper');
    }
  }

  async deleteShipper(id: string) {
    try {
      const exist = await this.prisma.shipper.findUnique({ where: { id } });
      if (!exist) {
        throw new NotFoundException('Shipper không tồn tại');
      }

      await this.prisma.shipper.delete({ where: { id } });

      return { message: 'Xóa shipper thành công', id };
    } catch (error) {
      this.logger.error(`Lỗi khi xóa shipper id=${id}`, error.stack);
      throw new InternalServerErrorException(error.message || 'Lỗi khi xóa shipper');
    }
  }
}
