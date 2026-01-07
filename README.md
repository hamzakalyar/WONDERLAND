# 🎪 WONDERLAND - Premium Toystore E-commerce Platform

A full-featured Django e-commerce platform for a premium toystore with advanced features including order management, reviews, wishlists, vouchers, and returns.

## ✨ Features

### 🛒 Core E-commerce
- **Product Catalog** - Browse toys by category with advanced filtering
- **Shopping Cart** - Session-based cart with real-time updates
- **Secure Checkout** - Stripe payment integration
- **Order Management** - Complete order tracking and history
- **User Accounts** - Registration, login, profile management

### 🎁 Advanced Features
- **Voucher System** - Discount codes with automatic welcome vouchers
- **Wishlist** - Save favorite products for later
- **Customer Reviews** - 5-star rating system with moderation
- **Product Search** - Real-time autocomplete search
- **Returns & Exchanges** - Customer-initiated return requests
- **Order Tracking** - Track shipments with carrier integration

### 👨‍💼 Admin Features
- **Enhanced Admin Panel** - Custom admin interface
- **Order Management** - Status updates with email notifications
- **Review Moderation** - Approve, reject, or flag reviews
- **Sales & Discounts** - Easy sale management
- **Inventory Tracking** - Stock monitoring with low stock alerts
- **Return Processing** - Approve/reject return requests

### 🎨 User Experience
- **Premium Design** - Modern, elegant UI with glassmorphism effects
- **Responsive Layout** - Works perfectly on all devices
- **Dark Mode Ready** - Professional color scheme
- **Smooth Animations** - Micro-interactions and transitions
- **Toast Notifications** - Real-time feedback for all actions
- **Enhanced Sort Dropdown** - Premium filtering options

## 🚀 Tech Stack

- **Backend:** Django 5.0
- **Database:** SQLite (Development) / PostgreSQL (Production Ready)
- **Payment:** Stripe Integration
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Custom CSS with CSS Variables
- **Icons & Assets:** Custom SVG icons
- **Email:** Django Email Backend

## 📦 Installation

### Prerequisites
- Python 3.12+
- pip
- virtualenv (recommended)

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/hamzakalyar/WONDERLAND.git
cd WONDERLAND
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
STRIPE_PUBLIC_KEY=your-stripe-public-key
STRIPE_SECRET_KEY=your-stripe-secret-key
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Collect static files**
```bash
python manage.py collectstatic
```

8. **Run the development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the site!

## 🗂️ Project Structure

```
WONDERLAND/
├── accounts/          # User authentication & profiles
├── cart/             # Shopping cart functionality
├── orders/           # Order management & tracking
├── store/            # Product catalog & reviews
├── vouchers/         # Discount voucher system
├── wishlist/         # User wishlists
├── toystore/         # Main project settings
├── templates/        # Global templates
├── static/           # Collected static files
├── media/            # User-uploaded files
├── manage.py         # Django management script
└── requirements.txt  # Python dependencies
```

## 🎯 Key Functionality

### For Customers
- Browse and search for toys
- Add products to cart and wishlist
- Apply discount vouchers
- Secure checkout with Stripe
- Track orders in real-time
- Leave product reviews
- Request returns/exchanges
- Manage profile and preferences

### For Administrators
- Manage products and categories
- Process orders and update status
- Moderate customer reviews
- Create and manage vouchers
- Handle return requests
- Monitor inventory levels
- Send automated email notifications
- View sales analytics

## 🔐 Security Features

- CSRF protection enabled
- Password hashing with Django's built-in system
- Secure password change with current password verification
- Session-based authentication
- Input sanitization and validation
- Protected admin routes

## 📧 Email Notifications

Automated emails for:
- Welcome message with voucher code
- Order confirmation
- Order status updates (shipped, delivered)
- Return request confirmations

## 🎨 Design Philosophy

WONDERLAND follows a premium, elegant design approach:
- **Glassmorphism** - Modern semi-transparent UI elements
- **Smooth Animations** - Micro-interactions enhance UX
- **Consistent Theme** - Navy blue & gold color palette
- **Typography** - Playfair Display & Montserrat fonts
- **Accessibility** - WCAG compliant color contrast

## 📝 Database Models

### Core Models
- `User` - Extended Django user model
- `Product` - Product information with categories
- `Category` - Product categorization
- `Order` - Customer orders with status tracking
- `OrderItem` - Individual items in orders
- `Review` - Product reviews with moderation
- `Voucher` - Discount codes and usage tracking
- `Wishlist` - User saved products
- `ReturnRequest` - Product return management

## 🛠️ Configuration

### Django Settings
Update `toystore/settings.py` for production:
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Set up PostgreSQL database
- Configure AWS S3 for media files (optional)
- Set up proper email backend

### Stripe Configuration
1. Sign up at [stripe.com](https://stripe.com)
2. Get your API keys from the dashboard
3. Add keys to `.env` file
4. Test with Stripe test cards

## 🚀 Deployment

### Recommended Platforms
- **Heroku** - Easy Django deployment
- **Railway** - Modern platform with automatic deployments
- **DigitalOcean** - VPS with full control
- **AWS** - Scalable cloud infrastructure

### Pre-deployment Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up production database (PostgreSQL)
- [ ] Configure static files serving
- [ ] Set up environment variables
- [ ] Configure email backend
- [ ] Test Stripe in live mode
- [ ] Set up SSL certificate

## 📄 License

This project is created for educational purposes.

## 👨‍💻 Author

**Hamza Kalyar**
- Email: hamzaimtiaz9970@gmail.com
- GitHub: [@hamzakalyar](https://github.com/hamzakalyar)

## 🙏 Acknowledgments

Built with Django and modern web technologies to create a premium e-commerce experience.

---

⭐ **Star this repo if you find it helpful!**
