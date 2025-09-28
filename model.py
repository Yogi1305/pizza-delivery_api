from database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    Username = Column(String, index=True)
    Email = Column(String, unique=True, index=True)
    Password = Column(String, nullable=True)
    IsActive = Column(Boolean, default=False)
    Is_staff = Column(Boolean, default=False)
    # Fixed relationship name to match the back_populates in Order
    orders = relationship("Order", back_populates="user")
    
    def __repr__(self):
        return f"User(id={self.id}, Username={self.Username}, Email={self.Email}, IsActive={self.IsActive}, Is_staff={self.Is_staff})"


class Order(Base):
    ORDER_STATUS = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )
    PIZZA_SIZES = (
        ("SMALL", "Small"), 
        ("MEDIUM", "Medium"), 
        ("LARGE", "Large")
    )
    
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    Quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(ORDER_STATUS), default='PENDING')
    pizza_size = Column(ChoiceType(PIZZA_SIZES), default="SMALL")
    flavor = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    # Fixed back_populates to match the relationship name in User
    user = relationship("User", back_populates="orders")
    
    def __repr__(self):
        return f"Order(id={self.id}, Quantity={self.Quantity}, order_status={self.order_status}, pizza_size={self.pizza_size}, flavor={self.flavor}, user_id={self.user_id})"