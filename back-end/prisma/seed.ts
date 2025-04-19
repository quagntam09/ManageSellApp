import { PrismaClient } from '@prisma/client';
import 'dotenv/config';
import { roles } from '../src/configs/config.json';
import * as bcrypt from 'bcryptjs'; // Thêm thư viện bcrypt để mã hóa mật khẩu

const prisma = new PrismaClient();

async function main() {
  const adminPassword = process.env.ADMIN_PASS;
  if (!adminPassword) {
    throw new Error("❌ Thiếu biến ADMIN_PASSWORD trong .env");
  }

  const hashedPassword = await bcrypt.hash(adminPassword, 10);
  const account = await prisma.account.upsert({
    where: { id: 'quagntam09' },
    update: {},
    create: {
      id: 'quagntam09',
      password: hashedPassword,
      roleId: "1000",
    },
  });

  await prisma.admin.upsert({
    where: { id: '0101' },
    update: {},
    create: {
      id: '0101',
      admin_name: 'Super Admin',
      account: {
        connect: { id: account.id },
      },
    },
  });

  console.log('✅ Seed admin thành công!');
  for (const role of roles) {
    await prisma.role.upsert({
      where: { id: role.role_id },
      update: {},
      create: {
        role_name: role.role_name,
        id: role.role_id
      }
    });
  }
  console.log('Seeded role thành công');
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(() => {
    prisma.$disconnect();
  });
